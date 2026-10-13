---
title: "ModelDoc2::GetCustomInfoValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCustomInfoValue.htm"
---

# ModelDoc2::GetCustomInfoValue

This method is obsolete and has been superseded by [ModelDocExtension::CustomPropertyManager](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__CustomPropertyManager.htm).

Description

This method gets the resolved custom information value.

Syntax (OLE Automation)

retval = ModelDoc2.GetCustomInfoValue ( configuration, FieldName )

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of the custom information |
| Return: | (BSTR) retval | Resolved value |

Syntax (COM)

status = ModelDoc2->GetCustomInfoValue ( configuration, FieldName, &retval )

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of the custom information |
| Output: | (BSTR) retval | Resolved value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If a custom information is associated with dimension name,

```vb
ModelDoc2.AddCustominfo2("Test","myDim", swCustomInfoText, "D1@Base-Extrude")
```

then

```vb
ModelDoc2.GetCustomInfoValue("Test","myDim")
```

returns the value of the dimension.

If the specified configuration is not the active configuration, the specified configuration becomes the active configuration and is assigned the custom information value. Then, the original configuration then becomes the active configuration.

To get a document-level property, pass an empty string ("") to the configuration argument.
