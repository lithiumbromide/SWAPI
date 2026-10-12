---
title: "GetEdges Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetEdges.html"
---

# GetEdges Method (IBody2)

Gets the edges for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetEdges()
```

### C#

```csharp
System.object GetEdges()
```

### C++/CLI

```cpp
System.Object^ GetEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [Body2::GetEdges](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetEdges.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)
[Display Vertices (VBA)](Display_Vertices_Example_VB.htm)
[Check Edges for Faults (C#)](Check_Edges_for_Faults_Example_CSharp.htm)
[Check Edges for Faults (VB.NET)](Check_Edges_for_Faults_Example_VBNET.htm)
[Check Edges for Faults (VBA)](Check_Edges_for_Faults_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetEdges.html)
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
