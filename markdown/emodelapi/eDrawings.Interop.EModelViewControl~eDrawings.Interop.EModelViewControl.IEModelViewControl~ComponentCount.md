---
title: "ComponentCount Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ComponentCount"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentCount.html"
---

# ComponentCount Property (IEModelViewControl)

Gets the number of components in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ComponentCount( _
   ByVal Config As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim Config As System.String
Dim value As System.Integer

value = instance.ComponentCount(Config)
```

### C#

```csharp
System.int ComponentCount(
   System.string Config
) {get;}
```

### C++/CLI

```cpp
property System.int ComponentCount {
   System.int get(System.String^ Config);
}
```

### Parameters

- `Config`: Name of the configuration for which to get the number of components or an empty string ("") or an asterisk ("*") (see Remarks)

### Property Value

Number of components in Config

## VBA Syntax

See [EModelViewControl::ComponentCount](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ComponentCount.html).

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

This property does not get the number of components for inactive component configurations of a top-level assembly in a SOLIDWORKS document. To get the number of components for inactive component configurations of a top-level assembly, you must use an eDrawings file that was published from SOLIDWORKS.

Passing an:

- Empty string ("") to Config gets the number of components in the active configuration.
- Asterisk ("*") to Config gets the number of components in all configurations.

You can also call [IEModelViewControl::ConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationName.html) to get the name of a configuration.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ComponentState](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentState.html)
[IEModelViewControl::ComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentName.html)
[IEModelViewControl::ComponentConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html)
[IEModelViewControl::ComponentTransform](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentTransform.html)
[IEModelViewControl::GetSelectedComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~GetSelectedComponentName.html)

## Availability

eDrawings API 2005 SP0
