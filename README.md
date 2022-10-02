<h1 align="center">Prntsc-Saver</h1>

## 👀 About
This is a script written in Python, which allows you to save random images from the site https://prnt.sc/. All images from the script go into a folder named images. The process might be quite slow due to the excess amount of empty and excluded images.

##  ❗ Warning
The images are obtained online from a site, which can be used by anyone and is not moderated. The content can be inappropriate and not safe for work. Use at your own risk!

## ⚙️ Properties
### 🚀 ID Generation
The method used for generating an id is simple. There's an array of all characters. It chooses 6 random characters from the array and searches for the image with that id. If it finds one and it isn't in the exclude folder, it saves it. Else it generates a new id and repeates. The average time for finding an image is around 4.2 seconds.

### 🔒 Exclude
All images in the exclude folder will be avoided from being selected. You can even add your own images!

### ✏️ Customization
You can edit all properties of the script in the properties.json file.

## 👨‍💻 Used technologies
<a href="https://code.visualstudio.com" target="_blank" rel="noreferrer"> <img src="https://img.icons8.com/color/344/visual-studio-code-2019.png" alt="python" width="50" height="50"/></a>
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="50" height="50"/></a>

## 🕹️ How to use
To use the script make sure you have Python installed. If you don't, click on the python icon and once you are in the installer, make sure to tick the `Add Python to PATH` box. If you do, you need to go into cmd and type `pip install {module}`. The modules you need are `opencv-python`, `requests`, `pathlib` and `pillow`. Once you've done that, just open the folder in cmd and type `python main.py` or if you want to, you can do the same in vscode.