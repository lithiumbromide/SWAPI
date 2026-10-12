---
title: "CurrentConfigurationIndex Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "CurrentConfigurationIndex"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentConfigurationIndex.html"
---

# CurrentConfigurationIndex Property (IEModelViewControl)

Gets the index number of this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentConfigurationIndex As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

value = instance.CurrentConfigurationIndex
```

### C#

```csharp
System.int CurrentConfigurationIndex {get;}
```

### C++/CLI

```cpp
property System.int CurrentConfigurationIndex {
   System.int get();
}
```

### Property Value

Index number of this configuration

## VBA Syntax

See [EModelViewControl::CurrentConfigurationIndex](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~CurrentConfigurationIndex.html).

## Remarks

Because eDrawings does not support inactive configurations for SOLIDWORKS documents, you must use an eDrawings file that was published from SOLIDWORKS.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ComponentCount](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentCount.html)
[IEModelViewControl::ComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentName.html)
[IEModelViewControl::ShowConfiguration](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowConfiguration.html)
[IEModelViewControl::ComponentConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html)
[IEModelViewControl::ConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationName.html)

## Availability

eDrawings API 2005 SP0
