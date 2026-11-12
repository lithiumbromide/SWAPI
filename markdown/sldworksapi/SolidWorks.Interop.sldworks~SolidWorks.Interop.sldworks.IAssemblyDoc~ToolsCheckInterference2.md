---
title: "ToolsCheckInterference2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ToolsCheckInterference2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.html"
---

# ToolsCheckInterference2 Method (IAssemblyDoc)

Checks for interference between parts in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ToolsCheckInterference2( _
   ByVal NumComponents As System.Integer, _
   ByVal LpComponents As System.Object, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef PComp As System.Object, _
   ByRef PFace As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim NumComponents As System.Integer
Dim LpComponents As System.Object
Dim CoincidentInterference As System.Boolean
Dim PComp As System.Object
Dim PFace As System.Object

instance.ToolsCheckInterference2(NumComponents, LpComponents, CoincidentInterference, PComp, PFace)
```

### C#

```csharp
void ToolsCheckInterference2(
   System.int NumComponents,
   System.object LpComponents,
   System.bool CoincidentInterference,
   out System.object PComp,
   out System.object PFace
)
```

### C++/CLI

```cpp
void ToolsCheckInterference2(
   System.int NumComponents,
   System.Object^ LpComponents,
   System.bool CoincidentInterference,
   [Out] System.Object^ PComp,
   [Out] System.Object^ PFace
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumComponents`: Number of components to check
- `LpComponents`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) being checked for interference
- `CoincidentInterference`: True to treat coincident entities as interference, false to not
- `PComp`: Array of components where interferences have been found
- `PFace`: Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) where interferences have been found

## VBA Syntax

See [AssemblyDoc::ToolsCheckInterference2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ToolsCheckInterference2.html).

## Examples

[Check Interference (VBA)](Check_Interference_using_AssemblyDoc_ToolsCheckInterference2_Example_VB.htm)

## Remarks

This method returns:

- an empty array of faces for components that have coincident faces that touch.
- an array of components for components that touch.

For each face that intersects, there is a corresponding component.

**NOTE:** The obsolete method, IAssemblyDoc::ToolsCheckInterference, displays the Interference Detection PropertyManager, but this method does not.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html)
[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IModeler::ICheckInterferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3.html)
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.html)
[IModeler::CheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
