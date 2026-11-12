---
title: "IToolsCheckInterference3 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IToolsCheckInterference3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html"
---

# IToolsCheckInterference3 Method (IAssemblyDoc)

Obsolete.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IToolsCheckInterference3( _
   ByVal NumComponents As System.Integer, _
   ByRef LpComponents As Component2, _
   ByVal CoincidentInterference As System.Boolean, _
   ByRef PComp As System.Object, _
   ByRef PFace As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim NumComponents As System.Integer
Dim LpComponents As Component2
Dim CoincidentInterference As System.Boolean
Dim PComp As System.Object
Dim PFace As System.Object

instance.IToolsCheckInterference3(NumComponents, LpComponents, CoincidentInterference, PComp, PFace)
```

### C#

```csharp
void IToolsCheckInterference3(
   System.int NumComponents,
   ref Component2 LpComponents,
   System.bool CoincidentInterference,
   out System.object PComp,
   out System.object PFace
)
```

### C++/CLI

```cpp
void IToolsCheckInterference3(
   System.int NumComponents,
   Component2^% LpComponents,
   System.bool CoincidentInterference,
   [Out] System.Object^ PComp,
   [Out] System.Object^ PFace
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumComponents`: Number of components to check
- `LpComponents`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) being checked for interference
- `CoincidentInterference`: True to check for coincident interference, false to not
- `PComp`: Array of components where interference has been found
- `PFace`: Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) where interference has been found

## VBA Syntax

See [AssemblyDoc::IToolsCheckInterference3](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IToolsCheckInterference3.html).

## Remarks

This method returns:

- an empty array of faces for components that have coincident faces that touch.
- an array of components for components that touch.

For each face that intersects, there is a corresponding component.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.html)
[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IModeler::CheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.html)
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.html)
[IModeler::ICheckInterferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
