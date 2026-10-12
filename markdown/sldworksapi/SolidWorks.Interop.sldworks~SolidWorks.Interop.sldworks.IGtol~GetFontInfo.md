---
title: "GetFontInfo Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFontInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFontInfo.html"
---

# GetFontInfo Method (IGtol)

Gets with the font information for this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFontInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Object

value = instance.GetFontInfo()
```

### C#

```csharp
System.object GetFontInfo()
```

### C++/CLI

```cpp
System.Object^ GetFontInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Object containing the font information (see **Remarks**)

## VBA Syntax

See [Gtol::GetFontInfo](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFontInfo.html).

## Remarks

Format of return value is an array of doubles. Currently this consists only of a [line type index](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::IGetFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFontInfo.html)
