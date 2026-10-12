---
title: "ReplacePLMComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ReplacePLMComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplacePLMComponents.html"
---

# ReplacePLMComponents Method (IAssemblyDoc)

Replaces a selected [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) component in this assembly with the specified component from a 3DEXPERIENCE collaborative space.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplacePLMComponents( _
   ByVal PLMID As System.String, _
   ByVal ConfigName As System.String, _
   ByVal ReplaceAllInstance As System.Boolean, _
   ByVal UseConfigChoice As System.Integer, _
   ByVal ReAttachMates As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim PLMID As System.String
Dim ConfigName As System.String
Dim ReplaceAllInstance As System.Boolean
Dim UseConfigChoice As System.Integer
Dim ReAttachMates As System.Boolean
Dim value As System.Boolean

value = instance.ReplacePLMComponents(PLMID, ConfigName, ReplaceAllInstance, UseConfigChoice, ReAttachMates)
```

### C#

```csharp
System.bool ReplacePLMComponents(
   System.string PLMID,
   System.string ConfigName,
   System.bool ReplaceAllInstance,
   System.int UseConfigChoice,
   System.bool ReAttachMates
)
```

### C++/CLI

```cpp
System.bool ReplacePLMComponents(
   System.String^ PLMID,
   System.String^ ConfigName,
   System.bool ReplaceAllInstance,
   System.int UseConfigChoice,
   System.bool ReAttachMates
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PLMID`: Unique ID of a replacement component in the collaboration space
- `ConfigName`: Name of a configuration (Physical Product) in the replacement component; an empty string indicates the default configuration of the replacement component
- `ReplaceAllInstance`: True to replace all instances of the selected components with the replacement component, false to not
- `UseConfigChoice`: Configuration to use as defined in [swReplaceComponentsConfiguration_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReplaceComponentsConfiguration_e.html)
- `ReAttachMates`: True to reattach any existing mates to the replacement component, false to not

### Return Value

True if the selected component is replaced, false if not

## VBA Syntax

See [AssemblyDoc::ReplacePLMComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ReplacePLMComponents.html).

## Remarks

Before calling this method, save any components that have been modified in this assembly. This method closes any open component files without saving modifications.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddPLMComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPLMComponent.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
