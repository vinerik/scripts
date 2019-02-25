###########
# get_propertie_from_user_list.ps1
# Desc: This script take alist of user and extract Active Directiry propertie
# Arg0: userlist.txt
# Return value : username, value of the propertie
# Return format: CSV
#####################

# Get user properties 
function GetUser_Propertie($username, $propertie1){
    $user_info = Get-ADUser $username.trim() -Properties $propertie1
    return $user_info
}

# Main #
$propertie=$args[0]


# From the users list get properties
foreach($line in Get-Content .\userlist.txt) {
        $clean_line=$line.trim()
        # Get the properties from AD
        $propertie_value=GetUser_Propertie "$clean_line" "$propertie"
        write-host $clean_line "," $propertie_value.$propertie
}
