#!/bin/bash
# Optimizer baseline tests
# 16 Mar 2018

# Note: Remember the slash at the end of the directory name
# testDir: directory with PDF optimizer tests
# exeDir: directory with PDF optimizer executable
# outDir: where to place output PDFs (these will be named after their respective tests)
# sysSlash: Use a forward or a backward slash
testDir=
exeDir=
outDir=
sysSlash="/"

[ -d $outDir ] || mkdir -p $outDir

echo "-----------------------------------"
echo "Executing Optimizer Baseline Tests"
echo "-----------------------------------"
echo
echo "Test File Directory:   "$testDir
echo "Optimizer Directory:  "$exeDir
echo "Output Directory:      "$outDir
echo 

# Remove >/dev/null to let pdfoptimizer print to console as it runs the tests
runTest () {
	echo "Running test: Process "$3" using "$2".json"
	$exeDir"optimizer" $testDir$1$sysSlash$3 $outDir$2"-"$3 $testDir$1$sysSlash$2".json" >/dev/null
}

# Expected format: Test_subfolder json_file_name test_pdf

echo "Cleanup tests - Optimize document"
runTest "Cleanup_Test" "Cleanup" "Multipage_10000_SaskTelBilling.pdf"
runTest "Cleanup_Test" "mobile_Cleanup" "Multipage_10000_SaskTelBilling.pdf"
echo

echo "Font tests - Subset embedded fonts and consolidate duplicate fonts"
runTest "Font_Test" "Font" "configom.pdf"
runTest "Font_Test" "mobile_Font_Test" "configom.pdf"
runTest "Font_Test" "Font" "parabolic.pdf"
runTest "Font_Test" "mobile_Font_Test" "parabolic.pdf"
echo

echo "Image tests - Downsample and recompress"
runTest "Image_Test" "Image" "Final-Fantasy-Adventure-Guide.pdf"
runTest "Image_Test" "mobile_Image_Test" "Final-Fantasy-Adventure-Guide.pdf"
runTest "Image_Test" "Image" "ImageResampling.pdf"
runTest "Image_Test" "mobile_Image_Test" "ImageResampling.pdf"
echo

echo "Objects tests - Discard bookmarks"
runTest "Objects_Test" "Objects" "physics_textbook.pdf"
runTest "Objects_Test" "mobile_Objects_Test" "physics_textbook.pdf"
echo

echo "Transparency tests - Set transparency to high-quality when optimizing"
runTest "Transparency_Test" "Transparency" "CreateTransparency.pdf"
runTest "Transparency_Test" "mobile_Transparency_Test" "CreateTransparency.pdf"
echo

echo "User data tests - Remove metadata, remove attachments and metadata, remove hyperlinks"
runTest "Userdata_Test" "Userdata" "AddDocumentInformation-meta.pdf"
runTest "Userdata_Test" "mobile_Userdata_Test" "AddDocumentInformation-meta.pdf"
runTest "Userdata_Test" "Userdata" "Attachments.pdf"
runTest "Userdata_Test" "mobile_Userdata_Test" "Attachments.pdf"
runTest "Userdata_Test" "Userdata" "AddLinks.pdf"
runTest "Userdata_Test" "mobile_Userdata_Test" "AddLinks.pdf"
echo

echo "ColorConversion tests - Perform color conversion"
runTest "Color_Conversion_Test" "ColorConversion" "ColorConversion.pdf"
runTest "Color_Conversion_Test" "mobile_ColorConversion" "ColorConversion.pdf"
echo

echo "PDFA1B conversion tests - Perform pdfa-1b conversion"
runTest "PDFA1B_Conversion_Test" "PDFA" "PDFA.pdf"
runTest "PDFA1B_Conversion_Test" "mobile_PDFA" "PDFA.pdf"
echo
