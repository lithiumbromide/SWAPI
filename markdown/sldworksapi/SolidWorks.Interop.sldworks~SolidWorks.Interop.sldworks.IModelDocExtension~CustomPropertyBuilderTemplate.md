---
title: "CustomPropertyBuilderTemplate Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CustomPropertyBuilderTemplate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyBuilderTemplate.html"
---

# CustomPropertyBuilderTemplate Property (IModelDocExtension)

Gets or sets the custom property builder template for this part.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomPropertyBuilderTemplate( _
   ByVal WeldmentTemplate As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim WeldmentTemplate As System.Boolean
Dim value As System.String

instance.CustomPropertyBuilderTemplate(WeldmentTemplate) = value

value = instance.CustomPropertyBuilderTemplate(WeldmentTemplate)
```

### C#

```csharp
System.string CustomPropertyBuilderTemplate(
   System.bool WeldmentTemplate
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ CustomPropertyBuilderTemplate {
   System.String^ get(System.bool WeldmentTemplate);
   void set (System.bool WeldmentTemplate, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WeldmentTemplate`: True if a weldment part, false if not (see **Remarks**)

### Property Value

File name of the custom property builder template (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::CustomPropertyBuilderTemplate](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CustomPropertyBuilderTemplate.html).

## Examples

```
swModDocExt.CustomPropertyBuilderTemplate(False) = "template.prtprp"
```

```
swModDocExt.CustomPropertyBuilderTemplate(True) = "templateWeld2.wldprp"
```

## Remarks

If WeldmentTemplate is:

- True, then this property gets or sets ***.wldprp**.
- False, then this property gets or sets ***.prtprp**.

All custom property builder templates are stored in the file location specified in **Tools > Options > File Locations > Custom Property Files**.

This property corresponds to the setting in the Template Options dialog that appears when you click on the button next to More Properties in the Custom Properties task pane. When you create a custom property layout, a template is created. The button is activated for parts and weldments only after a custom properties tab layout is created. The weldment custom property template (***.wldprp**) can be created or modified only if a cut list item is selected in the Cut list folder.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
