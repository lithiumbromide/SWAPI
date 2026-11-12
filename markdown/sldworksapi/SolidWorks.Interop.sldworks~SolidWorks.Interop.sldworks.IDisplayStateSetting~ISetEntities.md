---
title: "ISetEntities Method (IDisplayStateSetting)"
project: "SOLIDWORKS API Help"
interface: "IDisplayStateSetting"
member: "ISetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.html"
---

# ISetEntities Method (IDisplayStateSetting)

Sets the entities for this display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEntities( _
   ByVal EntityCount As System.Integer, _
   ByRef Entities As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayStateSetting
Dim EntityCount As System.Integer
Dim Entities As System.Object

instance.ISetEntities(EntityCount, Entities)
```

### C#

```csharp
void ISetEntities(
   System.int EntityCount,
   ref System.object Entities
)
```

### C++/CLI

```cpp
void ISetEntities(
   System.int EntityCount,
   System.Object^% Entities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityCount`: Number of entities in the Entities array
- `Entities`: - in-process, unmanaged C++: Pointer to an array of entities
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

After calling this method:

1. Call [IDisplayStateSetting::ISetNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetNames.html) to specify the display states.
2. Call [IDisplayStateSetting::Option](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Option.html) to specify the display state scope of the setting.
3. Get or set one or more of the following properties for the specified display states, components, and scope:
4. Call [IModelDocExtension::GetAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.html) to obtain an [IAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting.html) object.
5. Set the properties in the IAppearanceSetting object.
6. Get or set the material properties for the specified display states, components, and scope:

## See Also

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.html)
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html)
[IDisplayStateSetting::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.html)
[IDisplayStateSetting::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetEntities.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
