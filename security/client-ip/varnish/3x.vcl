sub vcl_recv {
    if (!req.http.true-client-ip) {
        if (req.http.X-Forwarded-For) {
            set req.http.True-Client-IP = req.http.x-forwarded-for;
        } else {
            set req.http.X-Forwarded-For = client.ip;
            set req.http.True-Client-IP = client.ip;
        }
    } else {
        set req.http.X-Forwarded-For = req.http.true-client-ip;
    }
}
