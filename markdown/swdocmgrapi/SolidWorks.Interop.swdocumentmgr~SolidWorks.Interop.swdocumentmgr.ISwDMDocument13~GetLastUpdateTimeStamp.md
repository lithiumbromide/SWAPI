---
title: "GetLastUpdateTimeStamp Method (ISwDMDocument13)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument13"
member: "GetLastUpdateTimeStamp"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetLastUpdateTimeStamp.html"
---

# GetLastUpdateTimeStamp Method (ISwDMDocument13)

Gets the last update stamp for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLastUpdateTimeStamp() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument13
Dim value As System.Integer

value = instance.GetLastUpdateTimeStamp()
```

### C#

```csharp
System.int GetLastUpdateTimeStamp()
```

### C++/CLI

```cpp
System.int GetLastUpdateTimeStamp();
```

### Return Value

Last update stamp in time_t format

## VBA Syntax

See [SwDMDocument13::GetLastUpdateTimeStamp](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument13~GetLastUpdateTimeStamp.html).

## Examples

[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)

## Remarks

The return value is in time_t format, which Microsoft defines "as time as seconds elapsed since midnight, January 1, 1970 or -1 in the case of error". You must either have built-in functions to convert this value to something more accessible or write your own functions.

## See Also

[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.html)
[ISwDMDocument13 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
