# Roadmap

 * Check that `pybars3` works with handlebars
   * Simple, nested interpolation
   * Loops
   * Helpers, maybe. Not sure
 * Check that `pyyaml` works with yaml
 * Make available interpolation inside yaml
   * example: `"${char.bar}"` --> `"*"`, when data is `{ char: { bar: "*" } }`
 * Decide format for:
   * yaml for single template asset
   * yaml for several templates parts asset
   * yaml for repository
 * Make sure that there's a function (and maybe cli entry) to
   * Process single asset
   * Process single repository
   * Process all assets/repositories

P.S. Everything but `py*` parts are for every language
