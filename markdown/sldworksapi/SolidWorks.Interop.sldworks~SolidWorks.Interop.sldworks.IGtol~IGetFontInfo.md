---
title: "IGetFontInfo Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetFontInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFontInfo.html"
---

# IGetFontInfo Method (IGtol)

Gets with the font information for this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFontInfo() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Double

value = instance.IGetFontInfo()
```

### C#

```csharp
System.double IGetFontInfo()
```

### C++/CLI

```cpp
System.double IGetFontInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Format of return value is an array of doubles. Currently this consists only of a [line type index](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetFontInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFontInfo.html)
