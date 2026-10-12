---
title: "GetPTZHeight2 Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetPTZHeight2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight2.html"
---

# GetPTZHeight2 Method (IGtol)

Gets the projected tolerance zone for the specified frame and tolerance in this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPTZHeight2( _
   ByVal FrameNumber As System.Integer, _
   ByVal TolNumber As System.Integer, _
   ByRef PtzDisplay As System.Boolean, _
   ByRef PtzHt As System.String _
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

value = instance.GetPTZHeight2(FrameNumber, TolNumber, PtzDisplay, PtzHt)
```

### C#

```csharp
System.bool GetPTZHeight2(
   System.int FrameNumber,
   System.int TolNumber,
   out System.bool PtzDisplay,
   out System.string PtzHt
)
```

### C++/CLI

```cpp
System.bool GetPTZHeight2(
   System.int FrameNumber,
   System.int TolNumber,
   [Out] System.bool PtzDisplay,
   [Out] System.String^ PtzHt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`: Frame number
- `TolNumber`: Tolerance number
- `PtzDisplay`: True if the projected zone tolerance is displayed in the GTol, false if not
- `PtzHt`: Height of the projected tolerance zone

### Return Value

True if the method executed successfully, false if not

## VBA Syntax

See [Gtol::GetPTZHeight2](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetPTZHeight2.html).

## Examples

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

## Remarks

This method:

- is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.
- returns the height of the projected tolerance zone as a string because it is a user-specified parameter that can be textual, numeric, or both types of data.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::SetPTZHeight2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPTZHeight2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
