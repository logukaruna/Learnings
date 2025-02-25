import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TextChange extends JFrame
{
	private 	JTextField inputField;
	private 	JTextArea displayArea;
	private JComboBox<String> fontComboBox;
	private JSpinner sizeSpinner;
	private JCheckBox boldCheckBox, italicCheckBox;

	public TextChange()
	{
		setTitle("Font Changer");
		setSize(400, 300);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLocationRelativeTo(null);

		inputField = new JTextField(20);
		displayArea = new JTextArea();
		displayArea.setEditable(true);
		displayArea.setLineWrap(true);

	String[] fonts= GraphicsEnvironment.getLocalGraphicsEnvironment().getAvailableFontFamilyNames();
		fontComboBox = new JComboBox<>(fonts);
		sizeSpinner = new JSpinner(new SpinnerNumberModel(12, 1, 100, 1));
		boldCheckBox = new JCheckBox("Bold");
		italicCheckBox = new JCheckBox("Italic");
		JButton applyButton = new JButton("Apply");

		JPanel controlPanel = new JPanel();
		controlPanel.add(new JLabel("Font:"));
		controlPanel.add(fontComboBox);
		controlPanel.add(new JLabel("Size:"));
		controlPanel.add(sizeSpinner);
		controlPanel.add(boldCheckBox);
		controlPanel.add(italicCheckBox);
		controlPanel.add(applyButton);

		add(inputField, BorderLayout.NORTH);
		add(controlPanel, BorderLayout.CENTER);
		add(new JScrollPane(displayArea), BorderLayout.SOUTH);

		applyButton.addActionListener(new ActionListener()
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				updateFont();
			}
		});
		inputField.addActionListener(new ActionListener()
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				updateFont();
			}
		});
	}
	private void updateFont()
	{
		String inputText = inputField.getText();
		displayArea.setText(inputText);

		String selectedFont = (String) fontComboBox.getSelectedItem();
		int fontSize = (Integer) sizeSpinner.getValue();
		int fontStyle = Font.PLAIN;

		if(boldCheckBox.isSelected())
		{
			fontStyle |= Font.BOLD;
		}
		if(italicCheckBox.isSelected())
		{
			fontStyle |= Font.ITALIC;
		}

		Font font = new Font(selectedFont, fontStyle, fontSize);
		displayArea.setFont(font);
	}
	public static void main(String[] args)
	{
		SwingUtilities.invokeLater(() ->
		{
			TextChange fontChange = new TextChange();
			fontChange.setVisible(true);
		});
	}
}