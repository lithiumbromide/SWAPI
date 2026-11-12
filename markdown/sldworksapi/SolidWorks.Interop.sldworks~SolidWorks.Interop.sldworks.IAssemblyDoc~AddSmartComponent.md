---
title: "AddSmartComponent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddSmartComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddSmartComponent.html"
---

# AddSmartComponent Method (IAssemblyDoc)

Adds the specified component at the specified coordinates as a Smart Component to this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSmartComponent( _
   ByVal CompName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Component2

value = instance.AddSmartComponent(CompName, X, Y, Z)
```

### C#

```csharp
Component2 AddSmartComponent(
   System.string CompName,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
Component2^ AddSmartComponent(
   System.String^ CompName,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompName`: Path and filename of the part document to add as a Smart Component
- `X`: X coordinate for the Smart Component
- `Y`: Y coordinate for the Smart Component
- `Z`: Z coordinate for the Smart Component

### Return Value

[Smart Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [AssemblyDoc::AddSmartComponent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddSmartComponent.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::CreateSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSmartComponent.html)
[IComponent2::GetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData.html)
[IComponent2::IsSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent.html)
[IComponent2::SetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSmartComponentData.html)
[ISmartComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
