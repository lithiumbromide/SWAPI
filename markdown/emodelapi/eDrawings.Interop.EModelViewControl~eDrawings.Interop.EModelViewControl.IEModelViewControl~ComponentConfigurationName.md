---
title: "ComponentConfigurationName Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ComponentConfigurationName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html"
---

# ComponentConfigurationName Property (IEModelViewControl)

Gets the name of the configuration for the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ComponentConfigurationName( _
   ByVal Config As System.String, _
   ByVal index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim Config As System.String
Dim index As System.Integer
Dim value As System.String

value = instance.ComponentConfigurationName(Config, index)
```

### C#

```csharp
System.string ComponentConfigurationName(
   System.string Config,
   System.int index
) {get;}
```

### C++/CLI

```cpp
property System.String^ ComponentConfigurationName {
   System.String^ get(System.String^ Config, System.int index);
}
```

### Parameters

- `Config`: Name of a component configuration in the top-level assembly or an asterisk ("*") for all component configurations in the top-level assembly (see **Remarks**)
- `index`: Index number of the component whose configuration name to get

### Property Value

Name of the configuration for the component

## VBA Syntax

See [EModelViewControl::ComponentConfigurationName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ComponentConfigurationName.html).

## Examples

Visual Basic code snippet that shows how to get the names of the components and the names of their component configurations in a top-level assembly configuration named Level1_Config2:

```
    count = Document.EModelViewControl.ComponentCount("Level1_Config2")
    for index = 0 to count
        componentName = Document.EModelViewControl.ComponentName("Level1_Config2", index)
        configurationName = Document.EModelViewControl.ComponentConfigurationName ("Level1_Config2", index)
        Debug.Print "Component name: " & componentName & " , Component configuration name: " & configurationName
    next
```

## Remarks

This property does not get component configuration names for inactive component configurations of a top-level assembly in a SOLIDWORKS document. To get the component configuration names for inactive component configurations of a top-level assembly, you must use an eDrawings file that was published from SOLIDWORKS.

Before calling this property, call:

- [IEModelViewControl::ConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationName.html) to get the name of a top-level assembly configuration.
- [IEModelViewControl::ComponentCount](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentCount.html) to get a valid value for index.
- [IEModelViewControl::ComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentName.html) so that you know which component refers to which configuration.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ComponentState](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentState.html)
[IEModelViewControl::ComponentTransform](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentTransform.html)
[IEModelViewControl::ConfigurationCount](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationCount.html)
[IEModelViewControl::CurrentConfigurationIndex](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentConfigurationIndex.html)
[IEModelViewControl::ShowConfiguration](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowConfiguration.html)
[IEModelViewControl::GetSelectedComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~GetSelectedComponentName.html)

## Availability

eDrawings API 2013 SP0
