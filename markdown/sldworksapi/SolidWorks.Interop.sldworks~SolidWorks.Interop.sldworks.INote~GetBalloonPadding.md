---
title: "GetBalloonPadding Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetBalloonPadding"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonPadding.html"
---

# GetBalloonPadding Method (INote)

Gets the balloon padding of this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBalloonPadding() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Double

value = instance.GetBalloonPadding()
```

### C#

```csharp
System.double GetBalloonPadding()
```

### C++/CLI

```cpp
System.double GetBalloonPadding();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Balloon padding

## VBA Syntax

See [Note::GetBalloonPadding](ms-its:sldworksapivb6.chm::/sldworks~Note~GetBalloonPadding.html).

## Examples

[Get BOM Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)
[Get BOM Balloon Properties (VB.NET)](Get_BOM_Balloon_Properties_Example_VBNET.htm)
[Get BOM Balloon Properties (C#)](Get_BOM_Balloon_Properties_Example_CSharp.htm)

## Remarks

This method is valid only if [INote::GetBalloonSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.html) is set to [swBalloonFit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html).swBF_Tightest.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::SetBalloonPadding Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloonPadding.html)
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
