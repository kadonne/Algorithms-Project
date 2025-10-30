$size = 0
$data_size = 40
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
    python Dan\make_data.py $size 5
    python Dan\decrypt.py
    "{0} {1}" -f "Trie-Tree:",$((Get-Content words.txt).Length)
}