# Porn Download Directory Categoriser (pddcat) 🐈
Organise your all-in-one everything's-a-jumbled-mess downloads directory into different directories based on models' names using regex. Check [functionality example](#functionality-example) below.

## HOW TO ❓
* Set path to your downloads and archive directories by running `-s` & `-d` options.
* Optionally download [curated_list](db/curated_list.txt) by running `-c`, otherwise it doesn't start with much data to work with.
* Then execute it without any parameters and watch your downloads directory untangle!
```
$ ./pddcat -s /path/to/src -d /path/to/dest
$ ./pddcat -c
$ ./pddcat
```

### USAGE
```
$ ./pddcat [-h] [-s path] [-d path] [-c] [-a name [name ...]]

Organise your all-in-one porn download directory into separate directories by model names.

optional arguments:
  -h, --help            show this help message and exit
  -s path, --source path
                        downloads dir where files are matched & moved from.
  -d path, --dest path  archive dir where directories with model names are
                        created & files moved to.
  -c, --curated-list    download a list of model names for a quick start.
  -a name [name ...], --add name [name ...]
                        add your own model names to a different file. use
                        underscore (_) in place of spaces and space to
                        separate more than one names. e.g. riley_reid bryci

```

### Contributing to model list
You can comment new names to [topic #9](https://github.com/kittenparry/pddcat/issues/9) or send a pull request to add more model names to [curated list](db/curated_list.txt) that you download with `-c` option.

#### Functionality Example
 * Source is `~/dwn` and destination is `~/arch`
 * `~/dwn/ariana.marie.awards.mp4` --> `~/arch/ariana_marie/ariana.marie.awards.mp4`
 * `~/dwn/bryci_youtube_playlist/` --> `~/arch/bryci/bryci_youtube_playlist/`
 * Meaning into their separate directories based on name.
 * `~/dwn/18.02.25.Lana.Rhoades.And.Jade.Nile.XXX.1080p/` --> `~/arch/lana_rhoades/18.02.25.Lana.Rhoades.And.Jade.Nile.XXX.1080p/`
   * `lana_rhoades` is longer than `jade_nile` in character length and gets checked, matched & moved to first. See [issue #4](https://github.com/kittenparry/pddcat/issues/4) for multiple models moving.

### NOTES
An uncorrectable shortcoming is it can't tell the difference between models with different names, for example `Nadya Nabakova` and `Bunny Colby` are the same person with different names/aliases. Depending on the file/directory name, it will put them into separate directories.

### LICENSING
`pddcat` is licensed under GNU General Public License v3.0 (GPL-3.0), see [LICENSE](LICENSE).
