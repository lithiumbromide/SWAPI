---
title: "mbsData Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRevComponent2"
member: "mbsData"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mbsData.html"
---

# mbsData Field

Format string entered in the administration tool if [mlEdmRevComponentFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2~mlEdmRevComponentFlags.html) contains the flag Edmrcf_TypeFormatString; if mbsDataField contains Edmrcf_TypeList, then the data member contains a new line-delimited list of list items.

## Syntax

### Visual Basic

```vb
Public mbsData As System.String
```

### C#

```csharp
public System.string mbsData
```

### C++/CLI

```cpp
public:
System.String^ mbsData
```

## Remarks

The mbsData member can contain the following format specifiers when mlEdmRevComponentFlags contains Edmrcf_TypeFormatString.

| Specifier | Meaning |
| --- | --- |
| %C | Uppercase A, B, C...Z |
| %c | Lowercase a, b, c...z |
| %01d | Number, 0-padded to 1 digit |
| %02d | Number, 0-padded to 2 digits, etc. |
| %01x | Lowercase hex number, 0-padded to 1 digit |
| %02x | Lowercase hex number, 0-padded to 2 digits, etc. |
| %01X | Uppercase hex number, 0-padded to 1 digit |
| %02X | Uppercase hex number, 0-padded to 2 digits, etc. |
| %4y | 4-digit year |
| %2y | 2-digit year |
| %01m | Month number without 0 padding (1-12) |
| %02m | Month number, 0-padded to two digits (01-12) |
| %01D | Day number without 0 padding (1-31) |
| %02D | Day number, 0-padded to 2 digits (00-31) |
| %01H | Hour without 0 padding (0-23) |
| %02H | Hour, 0-padded to 2 digits (00-23) |
| %01M | Minute without 0 padding (0-59) |
| %02M | Minute, 0-padded to 2 digits (00-59) |
| %01S | Second without 0 padding (0-59) |
| %02S | Second, 0-padded to 2 digits (00-59) |

## See Also

[EdmRevComponent2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2.html)
[EdmRevComponent2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRevComponent2_members.html)
