# Porn Download Directory Categoriser (pddcat)
Organise your download-everything-directory into named directories using regex. Check [HOW TO](#how-to) below.

### Usage:
```
$ ./pddcat [OPTIONS]
	
Options:
  -c, --curated-list	Download a list of model names for a quick start.
  -a, --add <m> <m2>...	Add your own model names to a different file.
			Use underscore (_) when a space is needed. e.g. riley_reid
			And spaces to separate different names. e.g. siri bryci
  -h, --help		Show this message and exit.
```

### Contributing to model list:

You can comment new names to topic [#9](https://github.com/kittenparry/pddcat/issues/9) or send a pull request to add more model names to [curated list](db/curated_list.txt) that you download with `-c` option.

## HOW TO
Edit `DWN_DIR` and `DEST_DIR` in program to use for your own needs.

**DWN_DIR:** User downloads directory (source), this is where you keep all your mumbled/jumbled downloads.  
**DEST_DIR:** User archive directory (destination), where named directories are created and your downloads get organised into.  
Example:  
 * DWN_DIR is `~/mydownloads`
 * DEST_DIR is `~/archive`
 * Your `ariana.marie.awards.mp4` file in `mydownloads` gets moved to `~/archive/ariana_marie/ariana.marie.awards.mp4`
 * Your `bryci_youtube_playlist` directory with everything inside intact in `mydownloads` gets moved to `~/archive/bryci/bryci_youtube_playlist/`
 * Meaning into their separate directories based on name.

How to edit variables:  
* Use either `os.path.join()` or a string at your own discreation.
* If using a string, DON'T END IN A SLASH (`/` or `\`)!
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
### Notes:

Some uncorrectable shortcomings:

* It can't tell the difference between `Nadya Nabakova` and `Bunny Colby`, who are the same person with different names/aliases. Depending on the file/directory name, it will put them into separate directories.

### LICENSING

The `pddcat` is licensed under GNU General Public License v3.0 (GPL-3.0), see [LICENSE](LICENSE).
