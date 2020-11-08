try {
    Remove-Item out.txt
}
catch {
    Write-Host ("file out.txt not found")
}

For ($i=1; $i -le 30; $i++) {
    java -cp .\jenetics-4.2.0.jar CW1_GA.java >> out.txt 
} 

