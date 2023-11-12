$size = 500
for ($i=1; $i -le 20; $i++) 
{
    python Ammar\make_data.py $size 5
    python Ammar\decrypt.py
    "{0} {1}" -f "Dictionary:",$((Get-Content words.txt).Length)
    $size = $size + 500

}
$size = 500
for ($i=1; $i -le 20; $i++) 
{
    python Kailey\make_data.py $size 5
    python Kailey\decrypt.py
    "{0} {1}" -f "Self-Balancing-Tree:",$((Get-Content words.txt).Length)
    $size = $size + 500

}
$size = 500
for ($i=1; $i -le 20; $i++) 
{
    python Dan\make_data.py $size 5
    python Dan\decrypt.py
    "{0} {1}" -f "Trie-Tree:",$((Get-Content words.txt).Length)
    $size = $size + 500
}