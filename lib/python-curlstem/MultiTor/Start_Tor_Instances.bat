SETLOCAL
SETLOCAL ENABLEDELAYEDEXPANSION
FOR /L %%G IN (10000, 10, 10100) DO (
 SET /a sp=%%G+1
 SET /a cp=%%G+10001
 echo !sp!
 echo !cp!
 mkdir data\tor-!sp!
 start bin\Tor\tor.exe GeoIPFile bin\Data\Tor\geoip GeoIPv6File bin\Data\Tor\geoip6 SOCKSPort 127.0.0.1:!sp! CONTROLPort 127.0.0.1:!cp! DATADirectory data\tor-!sp!
)
ENDLOCAL