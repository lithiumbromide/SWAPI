---
title: "AddPLMComponent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddPLMComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPLMComponent.html"
---

# AddPLMComponent Method (IAssemblyDoc)

Adds the specified component from a 3DEXPERIENCE collaborative space to the specified location in this assembly in [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPLMComponent( _
   ByVal PLMID As System.String, _
   ByVal ConfigName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim PLMID As System.String
Dim ConfigName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.AddPLMComponent(PLMID, ConfigName, X, Y, Z)
```

### C#

```csharp
System.object AddPLMComponent(
   System.string PLMID,
   System.string ConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ AddPLMComponent(
   System.String^ PLMID,
   System.String^ ConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PLMID`: Unique ID of a component
- `ConfigName`: Name of the configuration (Physical Product) from which to load the component
- `X`: X-coordinate of the component center
- `Y`: Y-coordinate of the component center
- `Z`: Z-coordinate of the component center

### Return Value

[IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [AssemblyDoc::AddPLMComponent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddPLMComponent.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ReplacePLMComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplacePLMComponents.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
