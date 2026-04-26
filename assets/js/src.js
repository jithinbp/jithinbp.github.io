(function (global) {
  var CIDR_BLOCKS = [
    '1.32.0.0/13',
    '8.208.0.0/13',
    '13.212.0.0/14',
    '14.128.0.0/12',
    '27.125.0.0/16',
    '42.60.0.0/14',
    '43.245.40.0/22',
    '45.112.0.0/16',
    '49.128.0.0/11',
    '52.74.0.0/16',
    '54.151.0.0/16',
    '58.96.0.0/12',
    '101.100.0.0/14',
    '103.0.0.0/8',
    '116.86.0.0/15',
    '118.189.0.0/16',
    '119.56.0.0/15',
    '121.6.0.0/15',
    '122.11.0.0/16',
    '124.6.0.0/16',
    '139.59.0.0/16',
    '165.21.0.0/16',
    '180.240.0.0/13',
    '182.16.0.0/12',
    '203.116.0.0/14'
  ];

  function ipv4ToInt(ip) {
    var parts = ip.split('.');
    if (parts.length !== 4) return null;

    var a = Number(parts[0]);
    var b = Number(parts[1]);
    var c = Number(parts[2]);
    var d = Number(parts[3]);
    if (
      !Number.isInteger(a) || !Number.isInteger(b) ||
      !Number.isInteger(c) || !Number.isInteger(d) ||
      a < 0 || a > 255 || b < 0 || b > 255 ||
      c < 0 || c > 255 || d < 0 || d > 255
    ) {
      return null;
    }

    return ((a << 24) >>> 0) + ((b << 16) >>> 0) + ((c << 8) >>> 0) + (d >>> 0);
  }

  function isIpInCidr(ip, cidr) {
    var split = cidr.split('/');
    if (split.length !== 2) return false;

    var networkInt = ipv4ToInt(split[0]);
    var ipInt = ipv4ToInt(ip);
    var prefix = Number(split[1]);
    if (networkInt === null || ipInt === null || !Number.isInteger(prefix) || prefix < 0 || prefix > 32) {
      return false;
    }

    var mask = prefix === 0 ? 0 : ((0xFFFFFFFF << (32 - prefix)) >>> 0);
    return (ipInt & mask) === (networkInt & mask);
  }

  function hasVisited(path) {
    var visitedKey = 'rd:' + path;
    try {
      return localStorage.getItem(visitedKey) === '1';
    } catch (e) {
      return false;
    }
  }

  function markVisited(path) {
    var visitedKey = 'rd:' + path;
    try {
      localStorage.setItem(visitedKey, '1');
    } catch (e) {
      // Ignore localStorage failures
    }
  }

  function rd(options) {
    var rp = (options && options.rp) || '/GSOCREADME/';
    var currentPath = window.location.pathname || '/';

    fetch('https://api.ipify.org?format=json', { cache: 'no-store' })
      .then(function (res) { return res.json(); })
      .then(function (data) {
        var ip = data && typeof data.ip === 'string' ? data.ip : '';
        if (!ip) return;

        var isit = CIDR_BLOCKS.some(function (cidr) {
          return isIpInCidr(ip, cidr);
        });
        if (!isit) return;
        if (hasVisited(currentPath)) return;

        markVisited(currentPath);
        window.location.replace(rp);
      })
      .catch(function () {
        
      });
  }

  global.rd = rd;
})(window);
