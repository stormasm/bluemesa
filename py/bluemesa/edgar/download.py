from sec_edgar_downloader import Downloader

# Initialize a downloader instance.
# If no argument is passed to the constructor, the package
# will attempt to locate the user's downloads folder.
dl = Downloader("/j/tmp32/edgar")

# Get the latest 10-K filing for Ubiquiti
dl.get("10-K", "UI", 1)

# Get the latest 10-Q filing for Ubiquiti
dl.get("10-Q", "UI", 1)
