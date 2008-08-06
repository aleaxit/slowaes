/*
* cryptoHelpers.js: implements AES - Advanced Encryption Standard
* from the SlowAES project, http://code.google.com/p/slowaes/
 * 
 * Copyright (c) 2008 	Josh Davis ( http://www.josh-davis.org ),
 * 						Johan Sundstrom ( http://ecmanaut.blogspot.com ),
 *			 			John Resig ( http://ejohn.org )
 * 
 * Licensed under the Apache License, Version 2.0
 * http://www.apache.org/licenses/
 */

var cryptoHelpers = {
	// encodes a unicode string to UTF8 (8 bit characters are critical to AES functioning properly)
	encode_utf8:function(s)
	{
		try{return unescape(encodeURIComponent(s));}
		catch(e){throw 'error during utf8 encoding: cryptoHelpers.encode_utf8.';}
	},
	
	// decodes a UTF8 string back to unicode
	decode_utf8:function(s)
	{
		try{return decodeURIComponent(escape(s));}
		catch(e){throw('error during utf8 decoding: cryptoHelpers.decode_utf8.');}
	},
	
	//convert a number array to a hex string
	toHex:function()
	{
		var array = [];
		if(arguments.length == 1 && arguments[0].constructor == Array)
			array = arguments[0];
		else
			array = arguments;
		var ret = '';
		for(var i = 0;i < array.length;i++)
			ret += (array[i] < 16 ? '0' : '') + array[i].toString(16);
		return ret.toLowerCase();
	},
	
	//convert a hex string to a number array
	toNumbers:function(s)
	{
		var ret = [];
		s.replace(/(..)/g,function(s){
			ret.push(parseInt(s,16));
		});
		return ret;
	},
	
	// get a random number in the range [min,max]
	getRandom:function(min,max)
	{
		if(min === null)
			min = 0;
		if(max === null)
			max = 1;
		return Math.round(Math.random()*max) + min;
	},
	
	generateSharedKey:function(len)
	{
		if(len === null)
			len = 16;
		var key = [];
		for(var i = 0; i < len*2; i++)
			key.push(this.getRandom(0,255));
		return key;
	},
	
	generatePrivateKey:function(s,size)
	{
		var sha = jsHash.sha2.arr_sha256(s);
		return sha.slice(0,size);
	}
};
