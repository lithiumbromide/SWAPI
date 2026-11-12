---
title: "ModelWindows Property (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "ModelWindows"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.html"
---

# ModelWindows Property (IFrame)

Gets the client model windows for this frame.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ModelWindows As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As System.Object

value = instance.ModelWindows
```

### C#

```csharp
System.object ModelWindows {get;}
```

### C++/CLI

```cpp
property System.Object^ ModelWindows {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of the client [model windows](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelWindow.html) of this frame

## VBA Syntax

See [Frame::ModelWindows](ms-its:sldworksapivb6.chm::/sldworks~Frame~ModelWindows.html).

## Examples

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
