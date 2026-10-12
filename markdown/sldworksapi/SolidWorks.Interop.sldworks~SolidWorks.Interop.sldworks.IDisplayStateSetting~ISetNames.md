---
title: "ISetNames Method (IDisplayStateSetting)"
project: "SOLIDWORKS API Help"
interface: "IDisplayStateSetting"
member: "ISetNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetNames.html"
---

# ISetNames Method (IDisplayStateSetting)

Sets the display state names for this display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetNames( _
   ByVal DsNameCount As System.Integer, _
   ByRef DSNames As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayStateSetting
Dim DsNameCount As System.Integer
Dim DSNames As System.String

instance.ISetNames(DsNameCount, DSNames)
```

### C#

```csharp
void ISetNames(
   System.int DsNameCount,
   ref System.string DSNames
)
```

### C++/CLI

```cpp
void ISetNames(
   System.int DsNameCount,
   System.String^% DSNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DsNameCount`: Number of names in the DSNames array
- `DSNames`: - in-process, unmanaged C++: Pointer to an array display state names
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

After calling this method:

1. Call [IDisplayStateSetting::ISetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetEntities.html) to specify the entities.
2. Call [IDisplayStateSetting::Option](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Option.html) to specify the display state scope of the setting.
3. Get or set one or more of the following properties for the specified display states, entities, and scope:

  - [IModelDocExtension::DisplayMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayMode.html)
  - [IModelDocExtension::Transparency](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Transparency.html)
  - [IModelDocExtension::Visibility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Visibility.html)
4. Call [IModelDocExtension::GetAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.html) to obtain an [IAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting.html) object.
5. Set the properties in the IAppearanceSetting object.
6. Get or set the material properties for the specified display states, entities, and scope:

  - [IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.html)

## See Also

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.html)
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html)
[IDisplayStateSetting::Names Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Names.html)
[IDisplayStateSetting::IGetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetNames.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
