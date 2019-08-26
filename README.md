# Porn Download Directory Categoriser (pddcat)
Organise your all-in-one everything's-a-jumbled-mess downloads directory into different directories based on models' names using regex. Check [HOW TO](#how-to) & [functionality example](#functionality-example) below.

I haven't tested it in Windows, but I'm fairly certain it should work without a hitch. Please send feedback to [topic #10](https://github.com/kittenparry/pddcat/issues/10) if you do.

### USAGE
```
$ ./pddcat [OPTIONS]
	
Options:
  -c, --curated-list	Download a list of model names for a quick start.
  -a, --add <m> <m2>...	Add your own model names to a different file.
			Use underscore (_) when a space is needed. e.g. riley_reid
			And spaces to separate different names. e.g. siri bryci
  -h, --help		Show this message and exit.
```

### Contributing to model list
You can comment new names to [topic #9](https://github.com/kittenparry/pddcat/issues/9) or send a pull request to add more model names to [curated list](db/curated_list.txt) that you download with `-c` option.

## HOW TO
Edit `DWN_DIR` and `DEST_DIR` in program to use for your own needs. See *functionality example* below.

**DWN_DIR:** User downloads directory (source), this is where you keep all your mumbled/jumbled downloads.  
**DEST_DIR:** User archive directory (destination), where named directories are created and your downloads get organised into.  

How to edit variables:  
* Use either `os.path.join()` or an absolute path string at your own discretion.
* If using a string, DON'T END IN A SLASH (`/` or `\`).
* `os.path.join()` is recommended.
* Use `os.path.expanduser('~')` to get get `$HOME`.

```python
# Examples
# Linux
DWN_DIR = os.path.join(os.path.expanduser('~'), 'path', 'to', 'dir')
DWN_DIR = os.path.join('/home', 'path', 'to', 'dir')
DWN_DIR = '/home/path/to/dir'

# Windows
DEST_DIR = os.path.join('c:/', 'path', 'to', 'dir')
DEST_DIR = 'c:/path/to/dir'
DEST_DIR = 'c:\path\\to\dir' # if you're into escapism
```

#### Functionality Example
 * DWN_DIR is `~/dwn`
 * DEST_DIR is `~/arch`
 * `~/dwn/ariana.marie.awards.mp4` --> `~/arch/ariana_marie/ariana.marie.awards.mp4`
 * `~/dwn/bryci_youtube_playlist/` --> `~/arch/bryci/bryci_youtube_playlist/`
 * `~/dwn/18.02.25.Lana.Rhoades.And.Jade.Nile.XXX.1080p/` --> `~/arch/lana_rhoades/18.02.25.Lana.Rhoades.And.Jade.Nile.XXX.1080p/`
   * `lana_rhoades` is longer than `jade_nile` in character length and gets checked, matched & moved to first. See [issue #4](https://github.com/kittenparry/pddcat/issues/4) for multiple models moving.
 * Meaning into their separate directories based on name.

### NOTES
An uncorrectable shortcoming is it can't tell the difference between `Nadya Nabakova` and `Bunny Colby`, who are the same person with different names/aliases. Depending on the file/directory name, it will put them into separate directories.

### LICENSING
`pddcat` is licensed under GNU General Public License v3.0 (GPL-3.0), see [LICENSE](LICENSE).
