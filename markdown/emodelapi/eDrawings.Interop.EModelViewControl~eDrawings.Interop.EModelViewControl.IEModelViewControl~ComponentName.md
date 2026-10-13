---
title: "ComponentName Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ComponentName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentName.html"
---

# ComponentName Property (IEModelViewControl)

Gets the name of the component in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ComponentName( _
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

value = instance.ComponentName(Config, index)
```

### C#

```csharp
System.string ComponentName(
   System.string Config,
   System.int index
) {get;}
```

### C++/CLI

```cpp
property System.String^ ComponentName {
   System.String^ get(System.String^ Config, System.int index);
}
```

### Parameters

- `Config`: Name of the configuration in which the component exists or an empty string ("") or an asterisk ("*") (see Remarks)
- `index`: Index number of the component to get

### Property Value

Name of the component

## VBA Syntax

See [EModelViewControl::ComponentName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ComponentName.html).

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

This property does not get component names for inactive component configurations of a top-level assembly in a SOLIDWORKS document. To get the component names for inactive component configurations of a top-level assembly, you must use an eDrawings file that was published from SOLIDWORKS.

Passing an:

- Empty string ("") to Config gets the name of the component at the specified index from the components in the active configuration.
- Asterisk ("*") to Config gets the name of the component at the specified index from the components in all configurations.

You can also call [IEModelViewControl::ConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationName.html) to get the name of a configuration.

Before calling this property call [IEModelViewControl::ComponentCount](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationCount.html) to get a valid value for Index.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ComponentConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html)
[IEModelViewControl::ComponentCount](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentCount.html)
[IEModelViewControl::ComponentState](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentState.html)
[IEModelViewControl::ComponentTransform](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentTransform.html)
[IEModelViewControl::GetSelectedComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~GetSelectedComponentName.html)

## Availability

eDrawings API 2005 SP0
