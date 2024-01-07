# config assets

### Intension

 * Describe assets, configs, bindings in yaml and handlebars
 * Enumerate needed repositories

### Roadmap

 * Decide format for (this part should be done once)
   * yaml for single template asset
   * yaml for several templates parts asset
   * yaml for repository

 * Check that language works with handlebars
   * Simple, nested interpolation
   * Loops
   * Helpers, maybe. Not sure

 * Check that language works with yaml
 * Make available interpolation inside yaml
   * example: `"${char.bar}"` --> `"*"`, when data is `{ char: { bar: "*" } }`

 * Check language for child process methods to run git clone

 * Make sure that there's a function (and maybe cli entry) to
   * Process single asset
   * Process single repository
   * Process all assets/repositories
