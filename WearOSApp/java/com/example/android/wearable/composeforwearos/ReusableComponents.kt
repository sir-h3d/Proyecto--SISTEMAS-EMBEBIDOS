package com.example.android.wearable.composeforwearos

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.size
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.CloudOff
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.wear.compose.material.Button
import androidx.wear.compose.material.ButtonDefaults
import androidx.wear.compose.material.Chip
import androidx.wear.compose.material.Icon
import androidx.wear.compose.material.MaterialTheme
import androidx.wear.compose.material.Text

@Composable
fun ChipExample(
    modifier: Modifier = Modifier,
    iconModifier: Modifier = Modifier, label: String, icono: ImageVector, function: () -> Unit
) {
    Chip(
        modifier = modifier,
        onClick = { function.invoke() },
        label = {
            Text(
                text = label,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
        },
        icon = {
            Icon(
                imageVector = icono,
                contentDescription = "default",
                modifier = iconModifier
            )
        },
    )
}

// TODO: Create a Text Composable
@Composable
fun TextExample(modifier: Modifier = Modifier) {
    Text(
        modifier = modifier,
        textAlign = TextAlign.Center,
        color = MaterialTheme.colors.primary,
        text = stringResource(R.string.device_shape)
    )
}

@Composable
fun ButtonExample(
    modifier: Modifier = Modifier,
    iconModifier: Modifier = Modifier, function: () -> Unit
) {
    Row(
        modifier = modifier,
        horizontalArrangement = Arrangement.Center
    ) {
        // Button
        Button(
            modifier = Modifier.size(ButtonDefaults.LargeButtonSize),
            onClick = { function.invoke() },
        ) {
            Icon(
                imageVector = Icons.Rounded.CloudOff,
                contentDescription = "Apagao",
                modifier = iconModifier
            )
        }
    }
}





