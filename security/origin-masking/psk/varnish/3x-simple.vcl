# This is for Varnish 3.x
# Authentication is handled within the 'vcl_recv' sub-section.
# This is a simple approach which doesn't provide any alternative methods such as User/Pass.
sub vcl_recv {

	# Authentication is done with the X-SS-Auth header
	# Fetch it, and validate it. If it doesn't match, issue a 403
	#
	# NB: we allow matching of two keys - the current, and the previous, before erroring
	# This is to allow for key cycling.

    # Uncomment the next line, and comment the line below, if currently cycling the key
    # if (req.http.X-SS-Auth != "<preshared key>" && req.http.X-SS-Auth != "<previous preshared key>") { 
	if (req.http.X-SS-Auth != "<preshared key goes here>") {
		error 403 "Forbidden";
	}

}
