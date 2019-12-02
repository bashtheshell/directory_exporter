# Directory Exporter

## Inspiration

Since I was unable to find a way to download or export the directory information from the [website](https://my.gallaudet.edu/directory) probably for a good reason, I leveraged the [Selenium WebDriver](https://selenium.dev/), a web testing automation framework, to extract the desired information from it. I was able to collect each directory entry and export them in a CSV file.

## Getting Started

Before starting, you'd need the latest copy of [Google Chrome](https://www.google.com/chrome/) and [Python 3](https://www.python.org/downloads/) installed. You may use your preferred package manager (e.g. [Homebrew](https://brew.sh/)) to install Python.

For your convenience, you can copy and paste the below scripts directly in the terminal console. After running the script, you can expect to see the resulting CSV file with `.csv` extension in the directory. The CSV file would contain a header row with fields delimited by semi-colon (`;`) character.

### For macOS: 

To setup:

```
# Download this repo 
git clone https://github.com/bashtheshell/directory_exporter.git
cd ./directory_exporter

# Set up Python environment
python3 -m venv venv
source ./venv/bin/activate

# Install Selenium
pip install --upgrade pip
pip install selenium

# Check if 'Google Chrome' exist
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version > /dev/null 2>&1
if [[ $? -eq 0 ]]
then
	# Download the compatible ChromeDriver to use with Selenium
	chrome_ver=$(/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version | awk '{ print $NF }' | sed 's/\..*$//')
	chromedriver_ver=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${chrome_ver})
	curl -s -o chromedriver_mac64.zip https://chromedriver.storage.googleapis.com/${chromedriver_ver}/chromedriver_mac64.zip
	unzip -oq chromedriver_mac64.zip

	# Run the main program
	python ./directory_exporter.py
else
	echo '"Google Chrome" app not found in /Applications folder.'
fi

```

To clean up:

```
# Leave virtual environment (venv)
deactivate

# Remove directory
cd ../
rm -rf ./directory_exporter
```

</br>

---

### DISCLAIMER

<a name="disclaimer">1</a>: This GitHub repository is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Gallaudet University, or any of their subsidiaries or affiliates. All product and institution names are the registered trademarks of their original owners. The use of any trade name or trademark is for demonstration, identification, and reference purposes only and does not imply any association with the trademark holder of their product brand.
