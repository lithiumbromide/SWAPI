---
title: "SetPTZHeight2 Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetPTZHeight2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPTZHeight2.html"
---

# SetPTZHeight2 Method (IGtol)

Sets the projected tolerance zone for the specified frame and tolerance in this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPTZHeight2( _
   ByVal FrameNumber As System.Integer, _
   ByVal TolNumber As System.Integer, _
   ByVal PtzDisplay As System.Boolean, _
   ByVal PtzHt As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Integer
Dim TolNumber As System.Integer
Dim PtzDisplay As System.Boolean
Dim PtzHt As System.String
Dim value As System.Boolean

value = instance.SetPTZHeight2(FrameNumber, TolNumber, PtzDisplay, PtzHt)
```

### C#

```csharp
System.bool SetPTZHeight2(
   System.int FrameNumber,
   System.int TolNumber,
   System.bool PtzDisplay,
   System.string PtzHt
)
```

### C++/CLI

```cpp
System.bool SetPTZHeight2(
   System.int FrameNumber,
   System.int TolNumber,
   System.bool PtzDisplay,
   System.String^ PtzHt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`: Frame number
- `TolNumber`: Tolerance number
- `PtzDisplay`: True to display the projected zone tolerance, false to not
- `PtzHt`: Height of the projected tolerance zone

### Return Value

True if this method executed successfully, false if not

## VBA Syntax

See [Gtol::SetPTZHeight2](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetPTZHeight2.html).

## Examples

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

## Remarks

This method is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.

The projected tolerance zone (PTZ) displays in the first tolerance window of the first control frame of the GTol. If PtzHt is not empty, its value is displayed after the PTZ symbol, which is a P enclosed in a circle.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetPTZHeight2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
