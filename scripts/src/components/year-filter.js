import $ from 'jquery'
import { chain, pick, omit, filter as lodashFilter, defaults } from 'lodash'
import TmplListGroupItem from '../templates/list-group-item'
import { setContent, slugify, createDatasetFilters, collapseListGroup } from '../util'

export default class YearFilter {
  constructor(opts) {
    const years = this._yearsWithCount(opts.datasets, opts.params)
    const yearsMarkup = years.map(TmplListGroupItem)
    setContent(opts.el, yearsMarkup)
    collapseListGroup(opts.el)
  }

  _yearsWithCount(datasets, params) {
    return chain(datasets)
      .map((dataset) => {
        const year = this._extractYear(dataset.start_date)
        if (!year) return null
        // Return a dataset object extended with a 'year' property
        return defaults({ year }, dataset)
      })
      .compact() // Remove any that does not have a valid year
      .groupBy('year')
      .map((datasetsInYear, yearValue) => {
        const filters = createDatasetFilters(pick(params, ['organization']))
        const filteredDatasets = lodashFilter(datasetsInYear, filters)
        const yearSlug = slugify(yearValue)
        const selected = params.year && params.year === yearSlug
        const itemParams = selected
          ? omit(params, 'year')
          : defaults({ year: yearSlug }, params)

        return {
          title: yearValue,
          url: '?' + $.param(itemParams),
          count: filteredDatasets.length,
          unfilteredCount: datasetsInYear.length,
          selected: selected
        }
      })
      .orderBy('unfilteredCount', 'desc')
      .value()
  }

  // Attempt to extract a 4-digit year from various date formats:
  // Possible formats:
  // - YYYY-MM-DD
  // - YYYY.MM.DD
  // - M/D/YYYY
  // - YYYY.M.D
  // - and variations thereof
  // If parsing fails, return null.
  _extractYear(startDate) {
    if (!startDate) return null

    // Trim whitespace just in case
    const dateStr = ('' + startDate).trim()

    // Try a few quick regex attempts to find a year:
    // Common patterns: 
    // - YYYY-MM-DD or YYYY.M.D or YYYY/M/D
    let match = dateStr.match(/^(\d{4})[-./]\d{1,2}[-./]\d{1,2}$/)
    if (match) return match[1]

    // Another pattern: YYYY-MM-DD HH-mm-ss
    match = dateStr.match(/^(\d{4})-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$/);
    if (match) return match[1];

    // Another pattern: M/D/YYYY
    match = dateStr.match(/(\d{4})$/)
    if (match && match[1].length === 4) return match[1]

    // As a last resort, try parsing with Date and extracting the year:
    const parsedDate = new Date(dateStr)
    if (!isNaN(parsedDate.valueOf())) {
      return '' + parsedDate.getFullYear()
    }

    // If all parsing attempts fail, return null
    return null
  }
}
