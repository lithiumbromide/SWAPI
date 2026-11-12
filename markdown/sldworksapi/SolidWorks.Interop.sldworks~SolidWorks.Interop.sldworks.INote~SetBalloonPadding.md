---
title: "SetBalloonPadding Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "SetBalloonPadding"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloonPadding.html"
---

# SetBalloonPadding Method (INote)

Sets the padding for this balloon note.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBalloonPadding( _
   ByVal Padding As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Padding As System.Double
Dim value As System.Boolean

value = instance.SetBalloonPadding(Padding)
```

### C#

```csharp
System.bool SetBalloonPadding(
   System.double Padding
)
```

### C++/CLI

```cpp
System.bool SetBalloonPadding(
   System.double Padding
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Padding`: Balloon padding

### Return Value

True if padding is successfully set, false if not

## VBA Syntax

See [Note::SetBalloonPadding](ms-its:sldworksapivb6.chm::/sldworks~Note~SetBalloonPadding.html).

## Remarks

This method is valid only if [INote::GetBalloonSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.html) is set to [swBalloonFit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html).swBF_Tightest.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetBalloonPadding Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonPadding.html)
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
