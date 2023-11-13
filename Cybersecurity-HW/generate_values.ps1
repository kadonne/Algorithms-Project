$size = 0
$data_size = 20
$size_increment = 100
#for ($i=1; $i -le $data_size; $i++) 
#{
#    $size = $size + $size_increment
#    python Ammar\make_data.py $size 5
#    python Ammar\decrypt.py
#    "{0} {1}" -f "Dictionary:",$((Get-Content words.txt).Length)
#
#}
#$size = 0
#for ($i=1; $i -le $data_size; $i++) 
#{
#    $size = $size + $size_increment
#    python Kailey\make_data.py $size 5
#    python Kailey\decrypt.py
#    "{0} {1}" -f "Self-Balancing-Tree:",$((Get-Content words.txt).Length)
#
#}
$size = 0
for ($i=1; $i -le $data_size; $i++) 
{
    $size = $size + $size_increment
    python Dan\make_data.py $size 5 32
    python Dan\decrypt.py 32
    "{0} {1}" -f "Character-length:", 32
    "{0} {1}" -f "Trie-Tree:",$((Get-Content words.txt).Length)
}

for ($i=1; $i -le $data_size; $i++) 
{
    $size = $size + $size_increment
    python Dan\make_data.py $size 5 40
    python Dan\decrypt.py 40
    "{0} {1}" -f "Character-length:", 40
    "{0} {1}" -f "Trie-Tree:",$((Get-Content words.txt).Length)
}

for ($i=1; $i -le $data_size; $i++) 
{
    $size = $size + $size_increment
    python Dan\make_data.py $size 5 56
    python Dan\decrypt.py 56
    "{0} {1}" -f "Character-length:", 56
    "{0} {1}" -f "Trie-Tree:",$((Get-Content words.txt).Length)
}

for ($i=1; $i -le $data_size; $i++) 
{
    $size = $size + $size_increment
    python Dan\make_data.py $size 5 64
    python Dan\decrypt.py 64
    "{0} {1}" -f "Character-length:", 64
    "{0} {1}" -f "Trie-Tree:",$((Get-Content words.txt).Length)
}

for ($i=1; $i -le $data_size; $i++) 
{
    $size = $size + $size_increment
    python Dan\make_data.py $size 5 96
    python Dan\decrypt.py 96
    "{0} {1}" -f "Character-length:", 96
    "{0} {1}" -f "Trie-Tree:",$((Get-Content words.txt).Length)
}