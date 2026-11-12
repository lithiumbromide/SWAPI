---
title: "UpdatesAllConfigurations Property (IEdmCardControl6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardControl6"
member: "UpdatesAllConfigurations"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6~UpdatesAllConfigurations.html"
---

# UpdatesAllConfigurations Property (IEdmCardControl6)

Gets whether this edit box control updates all configuration tabs of the file data card.

## Syntax

### Visual Basic

```vb
ReadOnly Property UpdatesAllConfigurations As System.Boolean
```

### C#

```csharp
System.bool UpdatesAllConfigurations {get;}
```

### C++/CLI

```cpp
property System.bool UpdatesAllConfigurations {
   System.bool get();
}
```

### Property Value

True to update all configuration tabs, false to not

## Examples

See the [IEdmCardControl6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6.html) examples.

## Remarks

This property:

- corresponds to the **Updates all configurations** check box in the Edit-box properties panel of the Card Editor.
- is valid only if [IEdmCardControl5::ControlType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5~ControlType.html) is [EdmCardControlType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardControlType.html).EdmCtrl_Editbox.

## See Also

[IEdmCardControl6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6.html)
[IEdmCardControl6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6_members.html)

## Availability

SOLIDWORKS PDM Professional 2015 SP02
