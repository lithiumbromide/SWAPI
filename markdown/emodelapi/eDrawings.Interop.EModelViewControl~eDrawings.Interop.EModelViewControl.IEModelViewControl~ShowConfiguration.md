---
title: "ShowConfiguration Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ShowConfiguration"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowConfiguration.html"
---

# ShowConfiguration Method (IEModelViewControl)

Displays the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowConfiguration( _
   ByVal ConfigurationIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim ConfigurationIndex As System.Integer

instance.ShowConfiguration(ConfigurationIndex)
```

### C#

```csharp
void ShowConfiguration(
   System.int ConfigurationIndex
)
```

### C++/CLI

```cpp
void ShowConfiguration(
   System.int ConfigurationIndex
)
```

### Parameters

- `ConfigurationIndex`: Index number of the configuration to display

## VBA Syntax

See [EModelViewControl::ShowConfiguration](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ShowConfiguration.html).

## Remarks

Because eDrawings does not support inactive configurations for SOLIDWORKS documents, this method does not get configurations for a SOLIDWORKS document (.**sldprt**, .**sldasm**, and .**slddrw**). To use configurations in eDrawings, you must use an eDrawings file that was published from SOLIDWORKS.

Before calling this method, call [IEModelViewControl::CurrentConfigurationIndex](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentConfigurationIndex.html) or [IEModelViewControl::ConfigurationCount](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationCount.html) to get a valid value for ConfigurationIndex.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ComponentConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html)
[IEModelViewControl::ComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentName.html)

## Availability

eDrawings API 2005 SP0
