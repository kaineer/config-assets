# TODO

 * Check that pybars3 works with handlebars
   * Simple, nested interpolation
   * Loops
   * Helpers, maybe. Not sure
 * Check that pyyaml works with yaml
 * Make available interpolation inside yaml
   * example: "${char.bar}" --> "*", when data is `{ char: { bar: "*" } }`
 * Make sure that there's a function (and maybe cli entry) to
   * Process single asset
   * Process single repository
   * Process all assets/repositories
