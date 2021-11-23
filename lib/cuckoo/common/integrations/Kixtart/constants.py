operators = {
    0x00: "and ",
    0x01: "BEEP ",
    0x02: "big ",
    0x03: "break ",
    0x04: "Call ",
    0x05: "case ",
    0x06: "cd ",
    0x07: "cls ",
    0x08: "color ",
    0x09: "cookie1 ",
    0x0A: "copy ",
    0x0B: "debug ",
    0x0C: "del ",
    0x0D: "DIM ",
    0x0E: "display ",
    0x0F: "do ",
    0x10: "each ",
    0x11: "endif ",
    0x13: "endselect ",
    0x14: "else ",
    0x15: "exit ",
    0x16: "file ",
    0x17: "float ",
    0x18: "flushkb ",
    0x19: "For ",
    0x1B: "get ",
    0x1C: "gets ",
    0x1D: "global ",
    0x1E: "go ",
    0x1F: "gosub ",
    0x21: "if ",
    0x20: "goto ",
    0x22: "in ",
    0x24: "integer ",
    0x25: "list ",
    0x26: "loop ",
    0x27: "md ",
    0x28: "mod ",
    0x29: "move ",
    0x2A: "Next ",
    0x2B: "Not ",
    0x2C: "or ",
    0x2D: "optional ",
    0x2E: "password ",
    0x2F: "play ",
    0x30: "preserve ",
    0x31: "Quit ",
    0x32: "redim ",
    0x33: "return ",
    0x34: "rd ",
    0x35: "Run ",
    0x36: "select ",
    0x37: "set ",
    0x38: "setl ",
    0x39: "setm ",
    0x3A: "settime ",
    0x3B: "shell ",
    0x3C: "sleep ",
    0x3D: "small ",
    0x3E: "step ",
    0x3F: "string ",
    0x40: "To ",
    0x41: "until ",
    0x42: "use ",
    0x43: "while ",
    0xD1: "=",
    0xC4: "*",
    0xC6: "+",
    0xC8: "&",
    0xC9: "|",
    0xCA: "^",
    0xCB: "~",
    0xCC: ",",
    0xCD: "(",
    0xCE: ")",
    0xC5: "/",
    0xC7: "-",
    0xCF: "[",
    0xD0: "]",
    0xD2: "<",
    0xD3: ">",
    0xD6: "==",
    0xE4: "?",
    0xD7: "<>",
    0xD4: "<=",
    0xD5: ">=",
}

functions = {
    0x00: "abs ",
    0x01: "asc ",
    0x02: "ascan ",
    0x03: "addkey ",
    0x04: "addprinterconnection ",
    0x05: "addprogramgroup ",
    0x06: "addprogramitem ",
    0x07: "at ",
    0x08: "backupeventlog ",
    0x09: "box ",
    0x0B: "chr ",
    0x0C: "cint ",
    0x0D: "cleareventlog ",
    0x0E: "close ",
    0x0F: "comparefiletimes ",
    0x10: "cstr ",
    0x11: "dectohex ",
    0x12: "delkey ",
    0x13: "delprogramgroup ",
    0x14: "delprogramitem ",
    0x15: "deltree ",
    0x16: "delvalue ",
    0x17: "delprinterconnection ",
    0x18: "dir ",
    0x19: "enumgroup ",
    0x1A: "enumipinfo ",
    0x1B: "enumkey ",
    0x1C: "enumlocalgroup ",
    0x1D: "enumvalue ",
    0x1E: "execute ",
    0x1F: "existkey ",
    0x20: "exist ",
    0x21: "expandenvironmentvars ",
    0x22: "fix ",
    0x23: "formatnumber ",
    0x24: "freefilehandle ",
    0x25: "getdiskspace ",
    0x26: "getfileattr ",
    0x27: "getfilesize ",
    0x28: "getfiletime ",
    0x29: "getfileversion ",
    0x2A: "getobject",
    0x2B: "iif ",
    0x2C: "ingroup ",
    0x2D: "instr ",
    0x2E: "instrrev ",
    0x2F: "int ",
    0x30: "isdeclared ",
    0x31: "join ",
    0x32: "kbhit ",
    0x33: "keyexist ",
    0x34: "lcase ",
    0x35: "left ",
    0x36: "len ",
    0x37: "loadkey ",
    0x38: "loadhive ",
    0x39: "logevent ",
    0x3A: "logoff ",
    0x3B: "ltrim ",
    0x3C: "makearray ",
    0x3D: "memorysize ",
    0x3E: "messagebox ",
    0x3F: "createobject",
    0x40: "open ",
    0x41: "readprofilestring ",
    0x42: "readline ",
    0x43: "readtype ",
    0x44: "readvalue ",
    0x45: "redirectoutput ",
    0x47: "right ",
    0x48: "replace ",
    0x48: "rnd ",
    0x49: "round ",
    0x4A: "rtrim ",
    0x4B: "savekey ",
    0x4C: "sendkeys ",
    0x4D: "sendmessage ",
    0x4E: "setascii ",
    0x4F: "setconsole ",
    0x50: "setdefaultprinter ",
    0x51: "setfocus ",
    0x52: "setfileattr ",
    0x53: "setoption ",
    0x54: "setsystemstate ",
    0x55: "settitle ",
    0x56: "setwallpaper ",
    0x57: "showprogramgroup ",
    0x58: "shutdown ",
    0x59: "sidtoname ",
    0x5A: "substr ",
    0x5B: "srnd ",
    0x5C: "split ",
    0x5D: "strdump ",
    0x5E: "trim ",
    0x5F: "ubound ",
    0x60: "ucase ",
    0x61: "unloadhive ",
    0x62: "val ",
    0x63: "vartype ",
    0x64: "vartypename ",
    0x65: "writeline ",
    0x66: "writeprofilestring ",
    0x67: "writevalue ",
    0x68: "getcommandline ",
}

macros = {
    0x01: "address ",
    0x02: "build ",
    0x04: "comment ",
    0x05: "cpu ",
    0x07: "csd ",
    0x08: "curdir ",
    0x09: "date ",
    0x0A: "day ",
    0x0B: "domain ",
    0x0C: "dos ",
    0x0D: "error ",
    0x0E: "serror ",
    0x0F: "fullname ",
    0x10: "homedir ",
    0x11: "homedrive ",
    0x12: "homeshr ",
    0x13: "hostname ",
    0x14: "im ",
    0x15: "IpAddress0 ",
    0x16: "IpAddress1 ",
    0x17: "IpAddress2 ",
    0x18: "IpAddress3 ",
    0x19: "kix ",
    0x1A: "inwin ",
    0x1B: "kq ",
    0x1C: "lanroot ",
    0x1D: "ldomain ",
    0x1E: "ldrive ",
    0x1F: "lm ",
    0x20: "logonmode ",
    0x21: "longhomedir ",
    0x22: "lserver ",
    0x23: "m0 ",
    0x24: "monthno ",
    0x25: "maxpwage ",
    0x26: "msecs ",
    0x29: "primarygroup ",
    0x2A: "priv ",
    0x2B: "productsuite ",
    0x2C: "producttype ",
    0x2D: "pwage ",
    0x2E: "ras ",
    0x30: "rserver ",
    0x31: "scriptdir ",
    0x33: "scriptname ",
    0x34: "sid ",
    0x35: "site ",
    0x36: "startdir ",
    0x37: "syslang ",
    0x39: "time ",
    0x3B: "userid ",
    0x3C: "userlang ",
    0x3D: "wdayno ",
    0x3E: "wksta ",
    0x3F: "wuserid ",
    0x40: "ydayno ",
    0x41: "ydayno ",
    0x42: "ydayno ",
    0xFF: "???",
}
