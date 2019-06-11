# Optimizer baseline tests
# python 3.7.2
import sys, os, shutil, subprocess
devnull = open(os.devnull, 'w')

# Expected format: Test_subfolder json_file_name test_pdf
def runTest(testFolder, testJson, testFile):
    print("    Running test", testJson, "with test file", testFile)
    subprocess.call(exeDir+" --input "+os.path.join(inDir, testFolder, testFile)+" --output "+os.path.join(outDir, testJson + "-" + testFile)+" --profile "+ os.path.join(inDir, testFolder, testJson)+".json", stdout=devnull)
    
def printUsage():
    print("Usage:", sys.argv[0], "<Optimizer-installation-directory> <test-pdf-directory> <output-file-directory>")

# Check arguments - use for number of arguments: len(sys.argv)

numArg = len(sys.argv)
if numArg < 4 or numArg > 4:
    print("Error: Incorrect number of arguments")
    printUsage()
    sys.exit()
else:
    exeDir = sys.argv[1]
    inDir = sys.argv[2]
    outDir = sys.argv[3]

print("Test file directory:   ", inDir)
print("Output file directory: ", outDir)

# Check input dir
if os.path.isdir(exeDir) == False:
    print("Exe directory not found at:", exeDir)
    sys.exit()

# Sort by OS
osType = os.name
if osType == "nt":
    exeDir = os.path.join(exeDir, "Optimizer.exe")
elif osType == "posix":
    exeDir = os.path.join(exeDir, "Optimizer")
else:
    print("Unsupported OS Type")
    sys.exit()

# Verify exe path
if os.path.isfile(exeDir) == False:
    print("Exe file not found at:", exeDir)
    sys.exit()

# Check input file directory
if os.path.isdir(inDir) == False:
    print("Input file directory not found at:", inDir)
    sys.exit()

# Check output file directory, clean if found, create if needed
if os.path.isdir(outDir) == True:
    print("Output directory found. Cleaning output directory...")
    counter = 0
    for root, dirs, files in os.walk(outDir):
        for file in files:
            if not file.endswith(".pdf"):
                counter += 1
    if counter > 0:
        print("Non pdf files found at output directory. Exiting without cleaning.")
        sys.exit()
    else:
        shutil.rmtree(outDir)
        os.mkdir(outDir)
else:
    print("Creating output directory...")
    try:
        os.mkdir(outDir)
    except OSError:
        print ("Creation of output directory failed")
    else:
        print ("Created output directory at:", outDir)

print("-------------------------------------")
print("Executing Optimizer Baseline Tests")
print("-------------------------------------")
print("Exe directory:         ", exeDir)
print("Test file directory:   ", inDir)
print("Output file directory: ", outDir)

print("Cleanup tests - Optimize document")
runTest("Cleanup_Test", "Cleanup", "Multipage_10000_SaskTelBilling.pdf")
runTest("Cleanup_Test", "mobile_Cleanup", "Multipage_10000_SaskTelBilling.pdf")
print("")

print("Font tests - Subset embedded fonts and consolidate duplicate fonts")
runTest("Font_Test", "Font", "configom.pdf")
runTest("Font_Test", "mobile_Font_Test", "configom.pdf")
runTest("Font_Test", "Font", "parabolic.pdf")
runTest("Font_Test", "mobile_Font_Test", "parabolic.pdf")
print("")

print("Image tests - Downsample and recompress")
runTest("Image_Test", "Image", "Final-Fantasy-Adventure-Guide.pdf")
runTest("Image_Test", "mobile_Image_Test", "Final-Fantasy-Adventure-Guide.pdf")
runTest("Image_Test", "Image", "ImageResampling.pdf")
runTest("Image_Test", "mobile_Image_Test", "ImageResampling.pdf")
print("")

print("Objects tests - Discard bookmarks")
runTest("Objects_Test", "Objects", "physics_textbook.pdf")
runTest("Objects_Test", "mobile_Objects_Test", "physics_textbook.pdf")
print("")

print("Transparency tests - Set transparency to high-quality when optimizing")
runTest("Transparency_Test", "Transparency", "CreateTransparency.pdf")
runTest("Transparency_Test", "mobile_Transparency_Test", "CreateTransparency.pdf")
print("")

print("User data tests - Remove metadata, remove attachments and metadata, remove hyperlinks")
runTest("Userdata_Test", "Userdata", "AddDocumentInformation-meta.pdf")
runTest("Userdata_Test", "mobile_Userdata_Test", "AddDocumentInformation-meta.pdf")
runTest("Userdata_Test", "Userdata", "Attachments.pdf")
runTest("Userdata_Test", "mobile_Userdata_Test", "Attachments.pdf")
runTest("Userdata_Test", "Userdata", "AddLinks.pdf")
runTest("Userdata_Test", "mobile_Userdata_Test", "AddLinks.pdf")
print("")

print("ColorConversion tests - Perform color conversion")
runTest("Color_Conversion_Test", "ColorConversion", "ColorConversion.pdf")
runTest("Color_Conversion_Test", "mobile_ColorConversion", "ColorConversion.pdf")
print("")

print("PDFA1B conversion tests - Perform pdfa-1b conversion")
runTest("PDFA1B_Conversion_Test", "PDFA", "PDFA.pdf")
runTest("PDFA1B_Conversion_Test", "mobile_PDFA", "PDFA.pdf")
print("")