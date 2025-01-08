import $ from 'jquery';
import { chain, pick, omit, filter, defaults } from 'lodash';

import TmplListGroupItem from '../templates/list-group-item';
import { setContent, slugify, createDatasetFilters, collapseListGroup } from '../util';

export default class DomainFilter {
  constructor(opts) {
    const domains = this._domainsWithCount(opts.datasets, opts.params);
    const domainsMarkup = domains.map(TmplListGroupItem);
    setContent(opts.el, domainsMarkup);
    collapseListGroup(opts.el);
  }

  // Given an array of datasets, returns an array of their domains with counts
  _domainsWithCount(datasets, params) {
    return chain(datasets)
      .filter('domain') 
      .flatMap(function (dataset) {
        // Explode objects where domain is an array into one object per domain
        if (typeof dataset.domain === 'string') return dataset;
        const duplicates = [];
        dataset.domain.forEach(function (domain) {
          duplicates.push(defaults({ domain }, dataset));
        });
        return duplicates;
      })
      .groupBy('domain') 
      .map(function (datasetsInDomain, domain) {
        const filters = createDatasetFilters(pick(params, ['organization']));
        const filteredDatasets = filter(datasetsInDomain, filters);
        const domainSlug = slugify(domain);
        const selected = params.domain && params.domain === domainSlug;
        const itemParams = selected
          ? omit(params, 'domain')
          : defaults({ domain: domainSlug }, params);
        return {
          title: domain,
          url: '?' + $.param(itemParams),
          count: filteredDatasets.length,
          unfilteredCount: datasetsInDomain.length,
          selected: selected,
        };
      })
      .orderBy('unfilteredCount', 'desc') 
      .value();
  }
}
