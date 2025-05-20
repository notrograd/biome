# biome
An open source package installer/build system.
<br>
# How can I use it?
Biome works by downloading from git, and searching for `biome.yml`. You can make a Biome compatible build system by uploading your project to git and adding a `biome.yml` file.
# biome.yml
Biome functions as a package installation tool and a build system. You can download source to your project, and upload your project to be downloaded. Biome is made to function without the need of a central package repository.
<br><br>
Heres how you should format your biome.yml: <br>
```yaml
biome:
  repositories:
  - github.com/Example/ExampleRepo # Biome will automatically put the source from repositories specified into /pkg/{repository name}
```
Thats it! All you need to get started with biome. 
# Notes
Biome is not a viable tool. Its something I'm gonna work on as a hobbie and as something I can learn more with. Maybe some day in 2088 Biome will become the next multilanguage build system. That day is not today.
