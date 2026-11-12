---
title: "SetPTZHeight Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetPTZHeight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPTZHeight.html"
---

# SetPTZHeight Method (IGtol)

Obsolete. Superseded by [IGtol::SetPTZHeight2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPTZHeight( _
   ByVal PtzHt As System.String, _
   ByVal DisplayIn As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim PtzHt As System.String
Dim DisplayIn As System.Boolean

instance.SetPTZHeight(PtzHt, DisplayIn)
```

### C#

```csharp
void SetPTZHeight(
   System.string PtzHt,
   System.bool DisplayIn
)
```

### C++/CLI

```cpp
void SetPTZHeight(
   System.String^ PtzHt,
   System.bool DisplayIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PtzHt`: Height of the projected tolerance zone
- `DisplayIn`: True to display the projected zone tolerance, false to not

## VBA Syntax

See [Gtol::SetPTZHeight](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetPTZHeight.html).

## Remarks

The projected tolerance zone (PTZ) displays in the first tolerance window of the first control frame of the GTol. If PtzHt is not empty, its value is displayed after the PTZ symbol, which is a P enclosed in a circle.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetPTZHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight.html)
