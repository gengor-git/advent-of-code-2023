$input_file = 'day01/input.txt'

$data = Get-Content -Path $input_file
$results = 0
foreach ($entry in $data) {
  $entry = $entry -replace "one", "o1e" `
    -replace "two", "t2o" `
    -replace "three", "t3e" `
    -replace "four", "f4r" `
    -replace "five", "f5e" `
    -replace "six", "s6x" `
    -replace "seven", "s7n" `
    -replace "eight", "e8t" `
    -replace "nine", "n9e" `

    $findings = Select-String -Pattern "\d" -InputObject $entry -AllMatches
    [string]$number = [string]$findings.Matches[0].Value + [string]$findings.Matches[-1].Value
    [int]$results += $number
}

Out-Default -InputObject $results