# Fetch the X-SS-Auth header
# If it matches our PSK, allow through
# Otherwise, issue a 403

# Current PSK - as provided by SwiftServe support
$curKey="<preshared key>"

# For use if you are currently cycling your keys
$oldKey="<old preshared key>"

if( (http.getHeader( "X-SS-Auth" ) != $curKey) && (http.getHeader( "X-SS-Auth" ) != $oldKey) ) { 

	http.sendResponse( "403 Forbidden", 
		"text/html", "Access denied\n", "" ); 
} 